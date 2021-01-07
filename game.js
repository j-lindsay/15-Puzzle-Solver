function find_blank_15p(start_state) {
  let ss_copy = start_state.slice();
  let blank = ss_copy.indexOf(0);
  let rowIndex = blank % 4;
  let colIndex = Math.floor(blank / 4);
  return [colIndex, rowIndex];
}

function actions_f_15p(start_state) {
  var actions = [];
  var blank = find_blank_15p(start_state);

  if (blank[1] != 0) {
    actions.append("left");
  }
  if (blank[1] != 3) {
    actions.append("right");
  }
  if (blank[0] != 0) {
    actions.append("up");
  }
  if (blank[0] != 3) {
    actions.append("down");
  }
  return actions;
}

function take_action_f_15p(start_state, action) {
  var ss_copy = start_state.slice();
  var blank = start_state.index(0);
  var actions = actions_f_15p(ss_copy);
  var temp = 0;

  if (action == "left" && action in actions) {
    temp = ss_copy[blank];
    ss_copy[blank] = ss_copy[blank - 1];
    ss_copy[blank - 1] = temp;
  }
  if (action == "right" && action in actions) {
    temp = ss_copy[blank];
    ss_copy[blank] = ss_copy[blank + 1];
    ss_copy[blank + 1] = temp;
  }
  if (action == "up" && action in actions) {
    temp = ss_copy[blank];
    ss_copy[blank] = ss_copy[blank - 4];
    ss_copy[blank - 4] = temp;
  }
  if (action == "down" && action in actions) {
    temp = ss_copy[blank];
    ss_copy[blank] = ss_copy[blank + 4];
    ss_copy[blank + 4] = temp;
  }
  return ss_copy;
}
