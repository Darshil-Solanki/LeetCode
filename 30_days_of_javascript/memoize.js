/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let memory = {}
    return function(...args) {
        let argsStr = "";
        for(let i = 0; i<args.length; i++){
            argsStr+=(args[i].toString()+"_");
        }
        if (argsStr in memory){
            return memory[argsStr];
        }
        memory[argsStr]=fn(...args);
        return memory[argsStr];
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
