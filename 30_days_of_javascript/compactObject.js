/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    let res;
    if(obj instanceof Array){
        res = [];
        obj.forEach((item)=>{
            if(item instanceof Array){
                let ans = compactObject(item);
                if(ans) res.push(ans);
            }else if(item instanceof Object){
                let ans = compactObject(item);
                if(ans) res.push(ans);
            }else
                if(item) res.push(item);
        });
    }else{
        res = {};
        for(let key in obj){
            if(obj[key] instanceof Array){
                let ans = compactObject(obj[key]);
                if(ans) res[key]=ans;
            }else if(obj[key] instanceof Object){
                let ans = compactObject(obj[key]);
                if(ans) res[key]=ans;
            }else
                if(obj[key]) res[key]=obj[key];
        }
    }
    return res;
};
