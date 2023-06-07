const oTableFilter = function () {
    var e, t = document.getElementsByTagName("table"),

        n = [];
    for (let g = 0; g < t.length; g++) {
        n[g] = document.getElementById(t[g].id), n[g].tr = n[g].getElementsByTagName("tr"), n[g].tr.length > 1 && (n[g].td = n[g].tr[1].getElementsByTagName("td"));
        for (let t = 0; t < n[g].td.length; t++) e = document.getElementById(n[g].id + t.toString()), n[g].input = [], null != e && (n[g].input[t] = document.getElementById(n[g].id + t.toString()), n[g].input[t].addEventListener("keyup", function () {
            l(n[g].id)
        }))
    }

    function l(e) {
        var t, n, l, g, d = [],
            m = [],
            o = [],
            a = [],
            r = !0;
        for (g = e, (t = document.getElementById(e).getElementsByTagName("tr")).length > 1 && (l = (d = t[1].getElementsByTagName("td")).length), n = 0; n < l; n++) null != document.getElementById(g + n.toString()) ? (m[n] = document.getElementById(g + n.toString()), o[n] = m[n].value.toUpperCase()) : l = n;
        for (n = 1; n < t.length; n++) {
            for (r = !0, j = 0; j < l; j++) a = (d = t[n].getElementsByTagName("td")[j]).textContent || d.innerText, "" != o[j] && a.toUpperCase().indexOf(o[j]) <= -1 && (r = !1);
            t[n].style.display = r ? "" : "none"
        }
    }
}();

function reloadPage() {
    var quantity = document.getElementById("quantity-dropdown").value;
    var currentURL = window.location.href;
    var updatedURL = currentURL.split("?")[0] + "?quantity=" + quantity;
    window.location.href = updatedURL;
}

function redirectToRegister() {
    window.location.href = "/register";
}

function redirectToLogin() {
    window.location.href = "/login";
}