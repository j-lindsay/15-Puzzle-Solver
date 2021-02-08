function parity(grid) {
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
var state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

console.log(parity(state))
