/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let val = init;
    return {
        "increment":()=>{return ++init},
        "decrement":()=>{return --init},
        "reset":()=>{init = val; return val}
    }
    let presentCount = init;

    // function increment() {
    //     return ++presentCount;
    // }

    // function decrement() {
    //     return --presentCount;
    // }

    // function reset() {
    //     return (presentCount = init);
    // }

    // return { increment, decrement, reset };
    // };

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
