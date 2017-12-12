


function Perceptron(iterations, printing_frequency) {
	var data_set = [
		[0, 0, 0, 1],
		[1, 0, 0, 1],
		[0, 1, 0, 1],
		[0, 0, 1, 1], 
		[1, 1, 0, 1], 
		[0, 1, 1, 1], 
		[1, 0, 1, 1],
		[1, 1, 1, 1]		
	];
	var expected = [0, 0, 0, 0, 0, 0, 1, 1];
	
	var nodes = [];
	var node_weights = [];
	var threshold = 0.5;
	
	// Set initial edge weights
	node_weights = defineRandomWeights(3);
	node_weights = node_weights.concat(-1);
	
	//console.log(data_set[0]);
	
	runSimulation(iterations, printing_frequency, data_set, expected, node_weights);
};

function defineRandomWeights(node_count) {
	var node_weights = []
	for (var i = 0; i < node_count; i++) {
		sign = 1;
		sign_number = Math.random();
		
		if (sign_number < 0.5) {
			sign = -1;
		}
		weight_value = sign * Math.random();
		
		node_weights = node_weights.concat(weight_value);
	}
	return node_weights;
};

function calculateSum(node_values, node_weights) {
	var sum = 0;
	for (var i = 0; i < node_values.length; i++) {
		sum += node_weights[i] * node_values[i];
	}
	return sum;
}

function sigmoidalFunction(x) {
	return 1 / (1 + Math.exp(-x));
}

function outputFunction(sum) {
	return sigmoidalFunction(sum);
}

function outputFunctionPrime(sum) {
	return sigmoidalFunction(sum) * (1 - sigmoidalFunction(sum));
	//return Math.exp(sum) / Math.pow(Math.exp(sum) + 1, 2);
}

function calculateError(output, expected) {
	return expected - output;
}

function adjustWeight(sum, error, node_value, node_weight) {
	var alpha = 0.01;
	//console.log("old_weight = " + node_weight + ", error = " + error + ", G'(sum) = " + outputFunctionPrime(sum)  + ", node_value = " + node_value);
	var new_weight = node_weight + alpha * error * outputFunctionPrime(sum) * node_value;
	//console.log("new_weight = " + new_weight + "\n");
	return new_weight;
}

function printWeights(iteration, node_weights) {
	console.log("Iteration: " + iteration + ", Weights = " + node_weights);
}

function printResults(data_set, expected, output) {
	console.log("data = " + data_set);
	console.log("expected = " + expected);
	console.log("predicted = " + output + "\n");
}

function runSimulation(iterations, printing_frequency, data_set, expected, node_weights) {
	var sum, output, error;
	
	/*console.log("data_set = " + data_set);
	console.log("expected  " + expected);
	console.log("weights = " + node_weights);*/
	for (var i = 0; i < iterations; i++) {
		if (i % printing_frequency == 0) {
			printWeights(i, node_weights);
		}
		for (var j = 0; j < data_set.length; j++) {
			sum = calculateSum(data_set[j], node_weights);
			output = outputFunction(sum);
			error = calculateError(output, expected[j]);
			
			if (i % printing_frequency == 0) {
				//printResults(data_set[j], expected[j], output);
			}
			/*console.log("data = " + data_set[j]);
			console.log("edge weights = " + node_weights + " (before)");
			console.log("sum = " + sum);
			console.log("output = " + output);
			console.log("error = " + error);*/
			for (var k = 0; k < node_weights.length-1; k++) {
				node_weights[k] = adjustWeight(sum, error, data_set[j][k], node_weights[k]);
			}
			/*console.log("edge_weights = " + node_weights + " (after) \n");*/
			/*if (i == iterations-1) {
				printResults(data_set[j], expected[j], output);
			}*/
		}
		
		
	}
}



function main() {
	new Perceptron(10000, 500);
}
main()
