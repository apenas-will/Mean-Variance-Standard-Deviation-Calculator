import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        data = np.array(list)
        data = data.reshape(3, 3)
        mean = [np.mean(data, axis=0).tolist(), np.mean(data, axis=1).tolist(), np.mean(data)]
        variance = [np.var(data, axis=0).tolist(), np.var(data, axis=1).tolist(), np.var(data)]
        standard_deviation = [np.std(data, axis=0).tolist(), np.std(data, axis=1).tolist(), np.std(data)]
        max_value = [np.max(data, axis=0).tolist(), np.max(data, axis=1).tolist(), np.max(data)]
        min_value = [np.min(data, axis=0).tolist(), np.min(data, axis=1).tolist(), np.min(data)]
        sum_values = [np.sum(data, axis=0).tolist(), np.sum(data, axis=1).tolist(), np.sum(data)]
        
        calculations = {
            'mean': mean,
            'variance': variance,
            'standard deviation': standard_deviation,
            'max': max_value,
            'min': min_value,
            'sum': sum_values
        }
        return calculations

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))