class Node {
  constructor(state, f = 0, g = 0, h = 0) {
    this.state = state;
    this.f = f;
    this.g = g;
    this.h = h;
  }
}

function AStarSearch(startState, actionsFunc, takeActionFunc, goalTestFunc, hFunc) {
  var h = hFunc(startState);
  var g = 0;
  startNode = Node((state = startState), (f = g + h), (g = g), (h = h));
  return AStarHelper(startNode, actionsFunc, takeActionFunc, goalTestFunc, hFunc, Number.MAX_VALUE);
}

function AStarHelper(parentNode, actionsFunc, takeActionFunc, goalTestFunc, hFunc, maxVal) {
  if (goalTestFunc(parentNode.state)) {
    return [[parentNode.state], parentNode.g];
  }

  var actions = actions_f(parentNode.state);
  if (!actions) {
    return ["failure", Number.MAX_VALUE];
  }

  var children = [];
  for (action in actions) {
    var [childState, stepCost] = takeActionFunc(parentNode.state, action);
    var g = parentNode.g + stepCost;
    var h = hFunc(childState);
    var f = Math.max(h + g, parentNode.f);
    childNode = Node((state = childState), (f = f), (g = g), (h = h));
    children.append(childNode);
  }

  while (true) {
    children = children.sort((a, b) => (a.f > b.f ? 1 : -1));
    bestChild = children[0];
    if (bestChild.f > maxVal) {
      return ["failure", bestChild.f];
    }

    var alternativeF;
    if (children.length > 1) {
      alternativeF = children[1].f;
    } else {
      alternativeF = Number.MAX_VALUE;
    }

    [result, bestChild.f] = AStarHelper(bestChild, actionsFunc, takeActionFunc, 
                                        goalTestFunc, hFunc, Math.max(maxVal, alternativeF));
    if (result != "failure") {
      result.unshift(parentNode.state);
      return [result, bestChild.f];
    }
  }
}
