var startBoard = {};
var endBoard = {};

startBoard.elements = {
    '1': document.getElementById('stile-1'),
    '2': document.getElementById('stile-2'),
    '3': document.getElementById('stile-3'),
    '4': document.getElementById('stile-4'),
    '5': document.getElementById('stile-5'),
    '6': document.getElementById('stile-6'),
    '7': document.getElementById('stile-7'),
    '8': document.getElementById('stile-8')
};

endBoard.elements = {
    '1': document.getElementById('etile-1'),
    '2': document.getElementById('etile-2'),
    '3': document.getElementById('etile-3'),
    '4': document.getElementById('etile-4'),
    '5': document.getElementById('etile-5'),
    '6': document.getElementById('etile-6'),
    '7': document.getElementById('etile-7'),
    '8': document.getElementById('etile-8')
};

function draw(Board, state) {
    state.split(' ').forEach(function(item, index) {
        if (item === '0') return;

        var element = Board.elements[item];
        var row = Math.floor(index / 3);
        var column = index % 3;

        element.style.top = (row * element.offsetHeight) + 'px';
        element.style.left = (column * element.offsetWidth) + 'px';
    });
}

draw(startBoard, '0 1 2 3 4 5 6 7 8');
draw(endBoard, '0 1 2 3 4 5 6 7 8');

document.getElementById('custom-start').value = '0 1 2 3 4 5 6 7 8';
document.getElementById('custom-end').value = '0 1 2 3 4 5 6 7 8';

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

function customStart() {
	var state = prompt("Please enter a starting state! (Example: 1 2 3 4 5 6 7 8 0)");

	if (state != null) {
		draw(startBoard, state);
	}
	document.getElementById('custom-start').value = state;
	document.getElementById('random-start').value = state;
}

function randomStart() {
	var state = ['0', '1', '2', '3', '4', '5', '6', '7', '8'];
	var joinedState = '';
	shuffle(state);

	if (state != null) {
		joinedState = state.join(' ');
		draw(startBoard, joinedState);
	}
	document.getElementById('random-start').value = joinedState;
	document.getElementById('custom-start').value = joinedState;
}

function customEnd() {
	var state = prompt("Please enter an ending state! (Example: 1 2 3 4 5 6 7 8 0)");

	if (state != null) {
		draw(endBoard, state);
	}
	document.getElementById('custom-end').value = state;
	document.getElementById('random-end').value = state;
}

function randomEnd() {
	var state = ['0', '1', '2', '3', '4', '5', '6', '7', '8'];
	var joinedState = '';
	shuffle(state);

	if (state != null) {
		joinedState = state.join(' ');
		draw(endBoard, joinedState);
	}
	document.getElementById('random-end').value = joinedState;
	document.getElementById('custom-end').value = joinedState;
}


function search() {
	
	const searchParams = {
		'custom-start': document.getElementById('custom-start').value,
		'random-start': document.getElementById('random-start').value,
		'custom-end': document.getElementById('custom-end').value,
		'random-end': document.getElementById('random-end').value,
		'algo': document.getElementById('algo').value,
		'heuristic': document.getElementById('heuristic').value,
		'max-depth': document.getElementById('max-depth').value,
		'depth-limit': document.getElementById('depth-limit').value
	};
	
	fetch('/receiver', {
		headers: {
		  'Content-Type': 'application/json'
		},
		method: 'POST',
		body: JSON.stringify({
			searchParams
		})
	}).then(function (response) { 
		return response.text();
	}).then(function (text) {

		console.log('POST response: ');
		console.log(text);
	});
	
	event.preventDefault();
} 

function reset() {
	draw(startBoard, '0 1 2 3 4 5 6 7 8');
	draw(endBoard, '0 1 2 3 4 5 6 7 8');
	document.getElementById('custom-start').value = '0 1 2 3 4 5 6 7 8';
	document.getElementById('random-start').value = '0 1 2 3 4 5 6 7 8';
	document.getElementById('custom-end').value = '0 1 2 3 4 5 6 7 8';
	document.getElementById('random-end').value = '0 1 2 3 4 5 6 7 8';
	document.getElementById('algo').value = 'select';
	document.getElementById('heuristic').value = 'select';
	document.getElementById('max-depth').value = '';
	document.getElementById('depth-limit').value = '';
}
