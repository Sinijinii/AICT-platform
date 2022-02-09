// form dynamic request for charts
document.body.addEventListener( 'click', function (event) {
    if( event.target.className === 'form-check-input dataset' ) {
        const form = event.target.form;
        const data = new FormData(form);

        const request = new XMLHttpRequest();
        request.open(form.method, form.action, true);
        request.send(data);

        request.addEventListener("load", function () {
            if (this.readyState === 4 && this.status === 200) {

                // catch JsonResponse from Django
                const response = JSON.parse(this.responseText);

                // display message
                const messages = document.getElementById("messages-list");
                messages.innerHTML += response.msg;
                fade_alerts();

                // load content
                const element = document.getElementById("demographics-content");
                const section = element.parentNode;
                section.removeChild(element);
                section.innerHTML = response.demographics;

                // extract variables for charts
                const label = response.label;
                const creation = response.creation;

                creationTime = returnCharts(label, creation);
                showCharts(creationTime);

            }
        });

    }
});