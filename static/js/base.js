Class = function(){};
Class.create = function(context) {
 var cls = function(){};
 cls.prototype = context || {};
 cls.create =  function(){
     var object = new cls();
     if (object.initialize)
         object.initialize.apply(object, arguments);
     return object;
 };
 return cls;
};

String.prototype.format = function(context){
    return this.replace(
        /\{\{([\.\w\-]+)\}\}/g,
        function(match, acessor){
            return context[acessor] || "";
        });
};

if(typeof String.prototype.trim !== 'function') {
  String.prototype.trim = function() {
    return this.replace(/^\s+|\s+$/g, ''); 
  };
}


function slugify(text) {
    text = text.replace(/[^-a-zA-Z0-9,&\s]+/ig, '');
    text = text.replace(/-/gi, "_");
    text = text.replace(/\s/gi, "-");
    return text;
}