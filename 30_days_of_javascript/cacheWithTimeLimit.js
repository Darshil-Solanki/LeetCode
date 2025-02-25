var TimeLimitedCache = function() {
    this.cache = new Map
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let flag = this.cache.has(key)
    if (flag) clearTimeout(this.cache.get(key).ref);
    this.cache.set(key, {value, ref:setTimeout(()=>this.cache.delete(key),duration)});
    return flag;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    try{
        return this.cache.get(key).value;
    }
    catch(err){
        return -1;
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
   return this.cache.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
