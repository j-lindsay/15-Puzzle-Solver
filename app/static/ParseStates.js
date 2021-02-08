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
