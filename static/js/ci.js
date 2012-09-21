ciItem = '<a href="{{url}}" class="ci-{{color}}">{{name}}</a>';

projetoItem = '<li id="{{slug_projeto}}" class="projetoItem"></li>';

PROJETOS = [];

function projetos(data){
    for (var i=0; i < data.jobs.length; i++) {
        PROJETOS[i] = data.jobs[i];
        PROJETOS[i]['slug_projeto'] =  slugify(data.jobs[i]['name']);
        $("#ci").append(projetoItem.format(PROJETOS[i]));
    }
}

$.getScript("http://busca.plataformas.glb.com/api/json?jsonp=projetos");

function atualizar_ci(data){
    var slug_projeto = slugify(data.name);
    $projeto = $("#{{slug_projeto}}".format({slug_projeto: slug_projeto}));
    var html = ciItem.format(data);
    $projeto.html(html);
}

setInterval(function(){
    for (var i=0; i < PROJETOS.length; i++) {
        var baseUrl = "http://busca.plataformas.glb.com/job/{{name}}/api/json?jsonp=atualizar_ci";
        var jenkinsUrl = baseUrl.format(PROJETOS[i]);
        $.getScript(jenkinsUrl);
    }
}, 2000);

// {
//     "actions": [
//     // {},
//     // {},
//     // {}
//     ],
//     "description": "Realiza a transformação do XML de visão de busca em JSON, formato compatível com a API do Elasticsearch.",
//     "displayName": "Conversor",
//     "name": "Conversor",
//     "url": "http://busca.plataformas.glb.com:8080/job/Conversor/",
//     "buildable": true,
//     "builds": [
//     {
//         "number": 43,
//         "url": "http://busca.plataformas.glb.com:8080/job/Conversor/43/"
//     }
//     ],
//     "color": "blue",
//     "firstBuild": {
//         "number": 43,
//         "url": "http://busca.plataformas.glb.com:8080/job/Conversor/43/"
//     },
//     "healthReport": [
//     {
//         "description": "Test Result: 0 tests failing out of a total of 7 tests.",
//         "iconUrl": "health-80plus.png",
//         "score": 100
//     },
//     {
//         "description": "Build stability: No recent builds failed.",
//         "iconUrl": "health-80plus.png",
//         "score": 100
//     }
//     ],
//     "inQueue": false,
//     "keepDependencies": false,
//     "lastBuild": {
//         "number": 43,
//         "url": "http://busca.plataformas.glb.com:8080/job/Conversor/43/"
//     },
//     "lastCompletedBuild": {
//         "number": 43,
//         "url": "http://busca.plataformas.glb.com:8080/job/Conversor/43/"
//     },
//     "lastFailedBuild": null,
//     "lastStableBuild": {
//         "number": 43,
//         "url": "http://busca.plataformas.glb.com:8080/job/Conversor/43/"
//     },
//     "lastSuccessfulBuild": {
//         "number": 43,
//         "url": "http://busca.plataformas.glb.com:8080/job/Conversor/43/"
//     },
//     "lastUnstableBuild": null,
//     "lastUnsuccessfulBuild": null,
//     "nextBuildNumber": 44,
//     "property": [
//     {
//         "wallDisplayName": null
//     }
//     ],
//     "queueItem": null,
//     "concurrentBuild": false,
//     "downstreamProjects": [],
//     "scm": {},
//     "upstreamProjects": []
// }
