import numpy as np
from scipy.signal import convolve2d
import os

def apply_gaussian_blur(image, kernel_size=(5, 5), sigma=1):
    """
    Gaussian Blur:
    - 사용 목적: 이미지의 노이즈를 줄이고 부드럽게 만듦.
    - 특징: 가우시안 분포를 기반으로 한 필터로, 가장 널리 사용되는 블러링 기법
    """
    def gaussian_kernel(size, sigma):
        ax = np.arange(-size // 2 + 1., size // 2 + 1.)
        xx, yy = np.meshgrid(ax, ax)
        kernel = np.exp(-(xx**2 + yy**2) / (2.*sigma**2))
        return kernel / np.sum(kernel)

    kernel = gaussian_kernel(kernel_size[0], sigma)

    return convolve2d(image, kernel, mode='same', boundary='symm')

def apply_median_blur(image, kernel_size=5):
    """
    Median Blur:
    - 사용 목적: 소금-후추 노이즈와 같은 특정 노이즈를 제거.
    - 특징: 커널 내의 픽셀 값을 정렬한 후 중간값을 선택하여 적용.
    """
    def median_filter_impl(data, kernel_size):
        height, width = data.shape
        pad_size = kernel_size // 2
        padded_data = np.pad(data, pad_size, mode='reflect')
        result = np.zeros_like(data)

        for i in range(height):
            for j in range(width):
                # 주변 픽셀을 정렬
                neighbors = padded_data[i:i+kernel_size, j:j+kernel_size].flatten()
                neighbors.sort()
                # 중간값을 선택
                result[i, j] = neighbors[kernel_size * kernel_size // 2]
        return result

    return median_filter_impl(image, kernel_size)

def apply_bilateral_filter(image, diameter=9, sigma_color=75, sigma_space=75):
    """
    Optimized Bilateral Filter:
    - 벡터화를 사용하여 연산 속도를 개선한 Bilateral 필터 구현.
    """
    half_diameter = diameter // 2
    padded_image = np.pad(image, half_diameter, mode='reflect')
    filtered_image = np.zeros_like(image, dtype=np.float64)

    # 공간적 가중치 계산 (고정된 값)
    x, y = np.meshgrid(np.arange(-half_diameter, half_diameter + 1), np.arange(-half_diameter, half_diameter + 1))
    spatial_weight = np.exp(-(x**2 + y**2) / (2 * sigma_space**2))

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # 주변 픽셀 추출
            region = padded_image[i:i + diameter, j:j + diameter]

            # 색상 차이에 따른 가중치 계산
            color_weight = np.exp(-((region - image[i, j])**2) / (2 * sigma_color**2))

            # 최종 가중치 계산
            combined_weight = spatial_weight * color_weight

            # 필터링 결과 계산
            filtered_image[i, j] = np.sum(combined_weight * region) / np.sum(combined_weight)

    return filtered_image.astype(np.uint8)

def apply_filter_to_rgb(image, filter_function, *args, **kwargs):
    """
    RGB 이미지를 처리하기 위한 헬퍼 함수.
    각 채널에 대해 필터를 개별적으로 적용한 후 다시 결합합니다.
    """
    # 채널 분리
    channels = [image[:, :, c] for c in range(image.shape[2])]
    
    # 각 채널에 필터 적용
    filtered_channels = [filter_function(channel, *args, **kwargs) for channel in channels]
    
    # 채널 결합
    return np.stack(filtered_channels, axis=-1)

# Example usage
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from skimage import io

    # 이미지 읽기 (RGB 이미지)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "example.jpg")
    image = io.imread(image_path)  # RGB 이미지로 읽기

    # 필터 적용 (예: Gaussian Blur)
    gaussian_blur_rgb = apply_filter_to_rgb(image, apply_gaussian_blur, kernel_size=(5, 5), sigma=1)
    median_blur_rgb = apply_filter_to_rgb(image, apply_median_blur, kernel_size=5)
    bilateral_filter_rgb = apply_filter_to_rgb(image, apply_bilateral_filter, diameter=9, sigma_color=75, sigma_space=75)

    # 결과 출력
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 1)
    plt.imshow(image)
    plt.title("Original RGB Image")

    plt.subplot(2, 3, 2)
    plt.imshow(gaussian_blur_rgb.astype(np.uint8))
    plt.title("Gaussian Blur (RGB)")

    plt.subplot(2, 3, 3)
    plt.imshow(median_blur_rgb.astype(np.uint8))
    plt.title("Median Blur (RGB)")

    plt.subplot(2, 3, 4)
    plt.imshow(bilateral_filter_rgb.astype(np.uint8))
    plt.title("Bilateral Filter (RGB)")

    plt.tight_layout()
    plt.show()