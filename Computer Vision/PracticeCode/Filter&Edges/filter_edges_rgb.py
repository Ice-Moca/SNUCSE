import numpy as np
from scipy.signal import convolve2d
import os

def apply_gaussian_blur(image, kernel_size=(5, 5), sigma=1):
    """
    Gaussian Blur:
    - 사용 목적: 이미지의 노이즈를 줄이고 부드럽게 만듦.
    - 특징: 가우시안 분포를 기반으로 한 필터로, 가장 널리 사용되는 블러링 기법
    - 시그마 값 커질수록 흐려진다.
    - 커널 크기가 커질수록 더 많은 픽셀을 고려하여 블러링 효과가 증가한다.
    - 평균 u 값이 0일때의 가우시안 블러의 구현
    - 노이즈 제거에 효과적이다.
    """
    def gaussian_kernel(size, sigma):
        ax = np.arange(-size // 2 + 1., size // 2 + 1.)
        # np.arange: 지정된 범위의 숫자를 생성하는 1차원 배열을 반환합니다.
        # 여기서는 -size//2 + 1부터 size//2까지의 값을 생성합니다.
        xx, yy = np.meshgrid(ax, ax)
        # np.meshgrid: 두 1차원 배열을 사용하여 2차원 좌표 그리드를 생성합니다.
        # xx는 x축 좌표를 반복하고, yy는 y축 좌표를 반복합니다.
        kernel = np.exp(-(xx**2 + yy**2) / (2.*sigma**2))
        # np.exp: 자연 상수 e의 거듭제곱을 계산합니다.
        # 여기서는 가우시안 함수의 값을 계산합니다.
        return kernel / np.sum(kernel)
        # np.sum: 배열의 모든 요소를 더한 값을 반환합니다.
        # 커널을 정규화하여 합이 1이 되도록 합니다.

    kernel = gaussian_kernel(kernel_size[0], sigma)

    return convolve2d(image, kernel, mode='same', boundary='symm')
    # scipy.signal.convolve2d: 2D 컨볼루션을 수행합니다.
    # mode='same': 출력 이미지의 크기를 입력 이미지와 동일하게 유지합니다.
    # boundary='symm': 경계 처리를 대칭적으로 수행합니다.

# Gaussian Blur:
# - Gaussian 커널을 생성한 후, 입력 이미지에 2D 컨볼루션을 적용하여 블러링 효과를 만듭니다.
# - 입력: 이미지, 커널 크기, 시그마 값
# - 출력: 블러링된 이미지

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
        # np.pad: 배열의 가장자리에 패딩을 추가합니다.
        # mode='reflect': 배열의 가장자리를 기준으로 대칭적으로 값을 복사합니다.
        result = np.zeros_like(data)
        # np.zeros_like: 입력 배열과 동일한 크기의 배열을 생성하며, 모든 요소를 0으로 초기화합니다.

        for i in range(height):
            for j in range(width):
                # 주변 픽셀을 정렬
                neighbors = padded_data[i:i+kernel_size, j:j+kernel_size].flatten()
                # np.flatten: 다차원 배열을 1차원 배열로 변환합니다.
                neighbors.sort()
                # 배열을 정렬하여 중간값을 선택합니다.
                result[i, j] = neighbors[kernel_size * kernel_size // 2]
        return result

    return median_filter_impl(image, kernel_size)

# Median Blur:
# - 커널 내의 픽셀 값을 정렬한 후 중간값을 선택하여 노이즈를 제거합니다.
# - 입력: 이미지, 커널 크기
# - 출력: 중간값 필터가 적용된 이미지

def apply_bilateral_filter(image, diameter=9, sigma_color=75, sigma_space=75):
    """
    Optimized Bilateral Filter:
    - 벡터화를 사용하여 연산 속도를 개선한 Bilateral 필터 구현.
    """
    half_diameter = diameter // 2
    padded_image = np.pad(image, half_diameter, mode='reflect')
    # np.pad: 입력 이미지에 패딩을 추가하여 경계 처리를 수행합니다.
    filtered_image = np.zeros_like(image, dtype=np.float64)
    # np.zeros_like: 입력 배열과 동일한 크기의 배열을 생성하며, 모든 요소를 0으로 초기화합니다.
    # dtype=np.float64: 계산 중 정밀도를 높이기 위해 64비트 부동소수점 타입을 사용합니다.

    # 공간적 가중치 계산 (고정된 값)
    x, y = np.meshgrid(np.arange(-half_diameter, half_diameter + 1), np.arange(-half_diameter, half_diameter + 1))
    # np.meshgrid: 2차원 좌표 그리드를 생성합니다.
    spatial_weight = np.exp(-(x**2 + y**2) / (2 * sigma_space**2))
    # np.exp: 공간적 거리 기반의 가중치를 계산합니다.

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
            # np.sum: 가중치와 픽셀 값을 곱한 결과를 합산하여 정규화합니다.

    return filtered_image.astype(np.uint8)
    # astype(np.uint8): 계산 결과를 8비트 정수로 변환하여 이미지로 저장할 수 있도록 합니다.

# Bilateral Filter:
# - 공간적 거리와 색상 차이를 기반으로 가중치를 계산하여 필터링을 수행합니다.
# - 입력: 이미지, 필터 직경, 색상 시그마, 공간 시그마
# - 출력: Bilateral 필터가 적용된 이미지
# - 참고: https://deep-learning-study.tistory.com/164

def apply_filter_to_rgb(image, filter_function, *args, **kwargs):
    """
    RGB 이미지를 처리하기 위한 헬퍼 함수.
    각 채널에 대해 필터를 개별적으로 적용한 후 다시 결합합니다.
    """
    # 채널 분리
    channels = [image[:, :, c] for c in range(image.shape[2])]
    # np.stack: 각 채널을 결합하여 RGB 이미지를 생성합니다.
    filtered_channels = [filter_function(channel, *args, **kwargs) for channel in channels]
    return np.stack(filtered_channels, axis=-1)

# apply_filter_to_rgb:
# - RGB 이미지를 처리하기 위해 각 채널에 필터를 개별적으로 적용합니다.
# - 입력: RGB 이미지, 필터 함수, 필터 함수의 추가 인자
# - 출력: 필터가 적용된 RGB 이미지


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