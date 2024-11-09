import numpy as np

# Define the input matrix with padding
input_matrix = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 4, 1, 0, 0],
    [0, 3, 1, 1, 0, 1, 0],
    [0, 2, 4, 1, 0, 1, 0],
    [0, 2, 0, 5, 2, 2, 0],
    [0, 0, 1, 3, 2, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

# Define the filter
filter_matrix = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

# Function to apply convolution
def apply_convolution(input_mat, filter_mat, stride, padding):
    # Calculate dimensions for output matrix
    output_size = (
        ((input_mat.shape[0] - filter_mat.shape[0] + 2 * padding) // stride) + 1,
        ((input_mat.shape[1] - filter_mat.shape[1] + 2 * padding) // stride) + 1
    )
    output_matrix = np.zeros(output_size)
    
    # Pad the input matrix
    padded_input = np.pad(input_mat, padding)
    
    # Perform the convolution
    for i in range(output_matrix.shape[0]):
        for j in range(output_matrix.shape[1]):
            output_matrix[i, j] = np.sum(
                filter_mat * padded_input[i*stride:i*stride+filter_mat.shape[0], j*stride:j*stride+filter_mat.shape[1]]
            )
    
    return output_matrix

# Apply convolutions
conv_stride_1 = apply_convolution(input_matrix, filter_matrix, stride=1, padding=1)
conv_stride_2 = apply_convolution(input_matrix, filter_matrix, stride=2, padding=1)

# Function to apply max pooling
def apply_max_pooling(input_mat, pool_size, stride):
    output_size = (
        (input_mat.shape[0] - pool_size) // stride + 1,
        (input_mat.shape[1] - pool_size) // stride + 1
    )
    output_matrix = np.zeros(output_size)
    
    for i in range(output_matrix.shape[0]):
        for j in range(output_matrix.shape[1]):
            output_matrix[i, j] = np.max(
                input_mat[i*stride:i*stride+pool_size, j*stride:j*stride+pool_size]
            )
    
    return output_matrix

# Max pooling on convolution with stride 1
max_pooling_result = apply_max_pooling(conv_stride_1, pool_size=3, stride=2)

conv_stride_1, conv_stride_2, max_pooling_result

print(conv_stride_1)

print(conv_stride_2)

print(max_pooling_result)
