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
	
	var startParity = parity(document.getElementById('custom-start').value);
	var endParity = parity(document.getElementById('custom-end').value);
	if (startParity != endParity) {
		alert("Error: The start state and goal state have different permuation parity. " +
			   "Try swapping an out of order tile on one of the states to achieve equal parity.")
		return;
	}
	
	fetch('/receiver', {
		headers: {
		  'Content-Type': 'application/json'
		},
		method: 'POST',
		body: JSON.stringify({
			searchParams
		})
	}).then(function (response) { 
		return response.json();
	}).then(function (json) {

		console.log('POST response: ');
		//console.log(json.result);
		solution_tree = flatToHierarchy(json.result)
		console.log(JSON.stringify(solution_tree, null, 4))
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

function parity(state) {
	var grid = state.split(/[,\s]+/g).map(Number)
    var inversions = 0;
    var arr = grid.slice(0);
    arr.splice(arr.indexOf(0), 1);

    for (var i = 1; i < arr.length; i++) {
        for (var j = i - 1; j >= 0; j--) {
            if (arr[j] <= arr[j+1]) break;
            [arr[j+1], arr[j]] = [arr[j], arr[j+1]];
            inversions++;
        };
    }
    return inversions & 1;
}

function flatToHierarchy(flat) {
    var roots = [] 
    var all = {}

    flat.forEach(function(item) {
      all[item.name] = item
    })

    Object.keys(all).forEach(function (name) {
        var item = all[name]
        if (item.parent === null) {
            roots.push(item)
        } else if (item.parent in all) {
            var p = all[item.parent]
            if (!('Children' in p)) {
                p.Children = []
            }
            p.Children.push(item)
        }
    })
    return roots
}
