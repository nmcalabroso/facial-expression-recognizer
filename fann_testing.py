from pyfann import libfann

connection_rate = 1
learning_rate = 0.5
num_input = 48*48
num_hidden = 100
num_output = 2

desired_error = 0.001
max_iterations = 1000
iterations_between_reports = 1

ann = libfann.neural_net()
ann.create_sparse_array(connection_rate, (num_input, num_hidden, num_output))
ann.set_learning_rate(learning_rate)
ann.set_activation_function_output(libfann.SIGMOID_SYMMETRIC)

ann.train_on_file("fann_train.data", max_iterations, iterations_between_reports, desired_error)

ann.save("fann_result_train.net")