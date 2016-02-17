$("pre").textContent.split(/\s+/).reduce((prev, curr, index) => {
    if (!curr) return prev;
    var dims = curr.split("x");
    dims.sort((a, b) => a - b);
    console.log(dims);
    return prev + 2 * (dims[0] + dims[1]) + dims[0] * dims[1] * dims[2];
}, 0)
