var sueString = document.querySelector("pre").textContent;

var analysis = {
    children: 3,
    cats: 7,
    samoyeds: 2,
    pomeranians: 3,
    akitas: 0,
    vizslas: 0,
    goldfish: 5,
    trees: 3,
    cars: 2,
    perfumes: 1
}

sueString.split("\n").map((sue, index) => {
    var re = /(\w+): (\d+)/g;
    var match;
    var props = { number: index + 1 };
    while ((match = re.exec(sue)) !== null) {
        props[match[1]] = +match[2]
    }
    return props;
}).filter(sue => Object.keys(sue).filter(key => key !== "number").every(key => {
    if (/cats|trees/.test(key)) {
        return sue[key] > analysis[key];
    }
    if (/pomeranians|goldfish/.test(key)) {
        return sue[key] < analysis[key];
    }
    return sue[key] === analysis[key];
}));

