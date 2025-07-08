import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    list_inputs = []
    
    for i in list:
        list_inputs.append(i)
    
    array_inputs = np.array(list_inputs)
    array_inputs = array_inputs.reshape(3,3)
    mean_rows_demo = array_inputs.mean(axis = 0)
    mean_rows = [float(x) for x in mean_rows_demo.tolist()]

    mean_columns_demo = array_inputs.mean(axis = 1)
    mean_columns = [float(x) for x in mean_columns_demo.tolist()]

    mean_flat = float(array_inputs.mean())

    var_rows_demo = array_inputs.var(axis = 0)
    var_rows = [float(x) for x in var_rows_demo.tolist()]

    var_columns_demo = array_inputs.var(axis = 1)
    var_columns = [float(x) for x in var_columns_demo.tolist()]

    var_flat = float(array_inputs.var())

    std_rows_demo = array_inputs.std(axis = 0)
    std_rows = [float(x) for x in std_rows_demo.tolist()]

    std_columns_demo = array_inputs.std(axis = 1)
    std_columns = [float(x) for x in std_columns_demo.tolist()]

    std_flat = float(array_inputs.std())

    max_rows_demo = array_inputs.max(axis = 0)
    max_rows = [float(x) for x in max_rows_demo.tolist()]

    max_columns_demo = array_inputs.max(axis = 1)
    max_columns = [float(x) for x in max_columns_demo.tolist()]

    max_flat = float(array_inputs.max())

    min_rows_demo = array_inputs.min(axis = 0)
    min_rows = [float(x) for x in min_rows_demo.tolist()]

    min_columns_demo = array_inputs.min(axis = 1)
    min_columns = [float(x) for x in min_columns_demo.tolist()]

    min_flat = float(array_inputs.min())

    sum_rows_demo = array_inputs.sum(axis = 0)
    sum_rows = [float(x) for x in sum_rows_demo.tolist()]

    sum_columns_demo = array_inputs.sum(axis = 1)
    sum_columns = [float(x) for x in sum_columns_demo.tolist()]

    sum_flat = float(array_inputs.sum())


    calculations = {
        'mean': [mean_rows, mean_columns, mean_flat], 
        'variance': [var_rows, var_columns, var_flat],
        'standard deviation': [std_rows, std_columns, std_flat],
        'max': [max_rows, max_columns, max_flat],
        'min': [min_rows, min_columns, min_flat],
        'sum': [sum_rows, sum_columns, sum_flat]
    }
    return calculations

