function renderImportContent() {
    //get template element and clone to clon
    var templateList = document.body.querySelectorAll("div[import]");
    //run throught the list and replace elements with templates
    for (var i = 0; i < templateList.length; i++) {
        //console.log(templateList[i].innerHTML);
        templateList[i].appendChild(fetchTemplate(templateList[i].getAttribute("import")));
    }
}

function fetchTemplate(path) {
    console.log('/html/template/'.concat(path));
    fetch('/html/template/'.concat(path)).then((response) =>{ return response.text();}).then((html) => { document.body.innerHTML = html}).catch((error) => {console.log("fetch error:", err)});
}
