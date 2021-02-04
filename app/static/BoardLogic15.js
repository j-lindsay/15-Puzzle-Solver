var Board = {};

Board.elements = {
    '1': document.getElementById('tile-1'),
    '2': document.getElementById('tile-2'),
    '3': document.getElementById('tile-3'),
    '4': document.getElementById('tile-4'),
    '5': document.getElementById('tile-5'),
    '6': document.getElementById('tile-6'),
    '7': document.getElementById('tile-7'),
    '8': document.getElementById('tile-8'),
    '9': document.getElementById('tile-9'),
    '10': document.getElementById('tile-10'),
    '11': document.getElementById('tile-11'),
    '12': document.getElementById('tile-12'),
    '13': document.getElementById('tile-13'),
    '14': document.getElementById('tile-14'),
    '15': document.getElementById('tile-15'),
};

Board.draw = function(state) {
    state.split(' ').forEach(function(item, index) {
        if (item === '0') return;

        var element = Board.elements[item];
        var row = Math.floor(index / 4);
        var column = index % 4;

        element.style.top = (row * element.offsetHeight) + 'px';
        element.style.left = (column * element.offsetWidth) + 'px';
    });
}

Board.draw('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15');

function shuffle(array) {
	var currentIndex = array.length, temporaryValue, randomIndex;
	
    while (0 !== currentIndex) {

        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

		temporaryValue = array[currentIndex];
		array[currentIndex] = array[randomIndex];
		array[randomIndex] = temporaryValue;
    }
	return array;
}

function customState() {
	var state = prompt("Please enter a starting state! (Example: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0");

	if (state != null) {
		Board.draw(state);
	}
	document.getElementById('custom-start').value = state;
	document.getElementById('random-start').value = state;
}

function randomState() {
	var state = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'];
	var joinedState = '';
	shuffle(state);

	if (state != null) {
		joinedState = state.join(' ');
		Board.draw(joinedState);
	}
	document.getElementById('random-start').value = joinedState;
	document.getElementById('custom-start').value = joinedState;
}


function search() {
	
	const searchParams = {
		'custom-start': document.getElementById('custom-start').value,
		'random-start': document.getElementById('random-start').value,
		'algo': document.getElementById('algo').value,
		'heuristic': document.getElementById('heuristic').value,
		'max-depth': document.getElementById('max-depth').value,
		'depth-limit': document.getElementById('depth-limit').value
	};
	
	fetch('/receiver', {

		// Declare what type of data we're sending
		headers: {
		  'Content-Type': 'application/json'
		},

		// Specify the method
		method: 'POST',

		// A JSON payload
		body: JSON.stringify({
			searchParams
		})
	}).then(function (response) { // At this point, Flask has printed our JSON
		return response.text();
	}).then(function (text) {

		console.log('POST response: ');

		// Should be 'OK' if everything was successful
		console.log(text);
	});
	// stop link reloading the page
	event.preventDefault();
} 

function reset() {
	Board.draw('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15');
	document.getElementById('custom-start').value = '';
	document.getElementById('random-start').value = '';
	document.getElementById('algo').value = 'select';
	document.getElementById('heuristic').value = 'select';
	document.getElementById('max-depth').value = '';
	document.getElementById('depth-limit').value = '';
}
