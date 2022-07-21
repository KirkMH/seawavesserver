function formatDate(date, withSec=false) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var secs = date.getSeconds();
    var ampm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    secs = secs < 10 ? '0'+secs : secs;
    var strTime = hours + ':' + minutes + (withSec) ? (':' + secs) : '' + ampm;
    return (date.getMonth()+1) + "/" + date.getDate() + "/" + date.getFullYear() + " " + strTime;
}