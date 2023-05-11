#!/usr/bin/node
exports.callMeMoby = (x, theFunction) => {
	for (i = 0; i < x; i++){
		theFunction();
	}
}
