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
