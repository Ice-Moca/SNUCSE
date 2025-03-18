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
    Bilateral Filter:
    - 사용 목적: 가장자리 정보를 보존하면서 노이즈를 제거.
    - 특징: 공간적 거리와 색상 차이를 모두 고려하여 필터링.
    """
    def bilateral_filter_pixel(i, j, diameter, sigma_color, sigma_space, img):
        half_diameter = diameter // 2
        filtered_pixel_weight_sum = 0
        weight_sum = 0
        pixel_value = img[i, j]

        for x in range(max(0, i - half_diameter), min(img.shape[0], i + half_diameter + 1)):
            for y in range(max(0, j - half_diameter), min(img.shape[1], j + half_diameter + 1)):
                neighbor_value = img[x, y]
                spatial_distance = np.sqrt((x - i)**2 + (y - j)**2)
                # 데이터 타입을 float64로 변경하여 overflow 방지
                color_distance = np.abs(neighbor_value.astype(np.float64) - pixel_value.astype(np.float64))

                spatial_weight = np.exp(-spatial_distance**2 / (2 * sigma_space**2))
                color_weight = np.exp(-color_distance**2 / (2 * sigma_color**2))
                weight = spatial_weight * color_weight

                filtered_pixel_weight_sum += neighbor_value * weight
                weight_sum += weight

        return filtered_pixel_weight_sum / weight_sum

    # 이미지 데이터 타입을 float64로 변경
    filtered_image = np.zeros_like(image, dtype=np.float64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            filtered_image[i, j] = bilateral_filter_pixel(i, j, diameter, sigma_color, sigma_space, image)

    return filtered_image.astype(np.uint8)

def apply_sobel_edge_detection(image, dx=1, dy=0, ksize=3):
    """
    Sobel Edge Detection:
    - 사용 목적: 이미지의 경계선을 검출.
    - 특징: x축 또는 y축 방향의 경계선을 강조.
    - x축 기준으로 경계선 강조 방식의 코드.
    """
    if ksize == 3:
        if dx == 1 and dy == 0:
            kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        elif dx == 0 and dy == 1:
            kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        else:
            raise ValueError("Invalid dx and dy values for ksize=3.  Use dx=1, dy=0 or dx=0, dy=1.")
    else:
        raise ValueError("Only ksize=3 is supported in this implementation.")

    return convolve2d(image, kernel, mode='same', boundary='symm')

def apply_laplacian_edge_detection(image, ksize=3):
    """
    Laplacian Edge Detection:
    - 사용 목적: 이미지의 경계선을 검출.
    - 특징: 2차 미분을 사용하여 경계선을 강조.
    """
    if ksize == 3:
        kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    else:
        raise ValueError("Only ksize=3 is supported in this implementation.")

    return convolve2d(image, kernel, mode='same', boundary='symm')

# Example usage
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from skimage import io

    # 이미지 읽기 (scikit-image 사용)
    # 현재 스크립트 파일의 디렉토리 가져오기
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 이미지 파일 경로 설정 (현재 디렉토리에 있는 example.jpg 파일)
    image_path = os.path.join(script_dir, "example.jpg")

    image = io.imread(image_path, as_gray=True) # scikit-image를 사용하여 grayscale로 읽기
    image = (image * 255).astype(np.uint8) # scikit-image는 0-1 사이의 float으로 읽으므로, 0-255로 변환

    # 필터 적용
    gaussian_blur = apply_gaussian_blur(image)
    median_blur = apply_median_blur(image)
    bilateral_filter = apply_bilateral_filter(image)
    sobel_edge = apply_sobel_edge_detection(image)
    laplacian_edge = apply_laplacian_edge_detection(image)

    # 결과 출력
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original")

    plt.subplot(2, 3, 2)
    plt.imshow(gaussian_blur, cmap='gray')
    plt.title("Gaussian Blur")

    plt.subplot(2, 3, 3)
    plt.imshow(median_blur, cmap='gray')
    plt.title("Median Blur")

    plt.subplot(2, 3, 4)
    plt.imshow(bilateral_filter, cmap='gray')
    plt.title("Bilateral Filter")

    plt.subplot(2, 3, 5)
    plt.imshow(sobel_edge, cmap='gray')
    plt.title("Sobel Edge Detection")

    plt.subplot(2, 3, 6)
    plt.imshow(laplacian_edge, cmap='gray')
    plt.title("Laplacian Edge Detection")

    plt.tight_layout()
    plt.show()