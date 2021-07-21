const brain = require('brain.js');
const data = require('./data/nba-2021.json');

const network = new brain.NeuralNetwork();

const trainingData = data.map(item => ({
    input: [item.Visitor, item.Home],
    output: [item.Winner]
}));

network.train(trainingData, {
    iterations: 2000
});

// [Visiting, Home]
const test = ['Phoenix Suns','Milwaukee Bucks']
const result = network.run(test);

if (result == 0) {
    console.log(`${test[0]} wins!`)
}
else {
    console.log(`${test[1]} wins!`)
}
// console.log(`Predicted Winner: ${result}`);