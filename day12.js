function iterate_keys(prev, curr, object) {
    const value = object[curr];

    if (typeof value === "number") {
        return prev + value;
    }

    if (typeof value === "string") {
        return prev;
    }

    if (!(value instanceof Array) && Object.keys(value).some(k => value[k] === "red")) {
        return prev;
    }

    return Object.keys(value).reduce((prev, curr) => iterate_keys(prev, curr, value), prev);
}

var parsed = JSON.parse(document.querySelector("pre").textContent);
var total = Object.keys(parsed).reduce((prev, curr) => iterate_keys(prev, curr, parsed), 0);
console.log(total);