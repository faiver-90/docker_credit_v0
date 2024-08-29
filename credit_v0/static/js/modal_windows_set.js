let alertQueue = [];
let isAlertShowing = false;

function enqueueAlert(message) {
    alertQueue.push(message);
    if (!isAlertShowing) {
        showNextAlert();
    }
}

function showNextAlert() {
    if (alertQueue.length > 0) {
        isAlertShowing = true;
        const message = alertQueue.shift();
        $('#alertModalBody').text(message);
        $('#alertModal').modal('show');
    } else {
        isAlertShowing = false;
    }
}

$('#alertModal').on('hidden.bs.modal', function () {
    showNextAlert();
    scrollToFirstInvalidField();
});

function showAlert(message) {
    $('#alertModalBody').text(message);
    $('#alertModal').modal('show');
}

function scrollToFirstInvalidField() {
    const firstInvalidField = document.querySelector('.form-control:invalid');
    if (firstInvalidField) {
        firstInvalidField.scrollIntoView({behavior: 'smooth', block: 'center'});
        firstInvalidField.focus();
    }
}
