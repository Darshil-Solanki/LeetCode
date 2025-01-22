class EventEmitter {
    events = {}
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (!(eventName in this.events))
            this.events[eventName]=[]
        this.events[eventName].push(callback)
        return {
            unsubscribe: () => {
                let idx = this.events[eventName].indexOf(callback);
                if (idx!==-1){
                    this.events[eventName].splice(idx,1);
                }
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        let res = [];
        if(eventName in this.events){
            this.events[eventName].forEach(item=>res.push(item(...args)));
        }
        return res;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
