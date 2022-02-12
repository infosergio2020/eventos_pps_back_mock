
class MenubarNavigation {
    constructor(e) {
        var t, i;
        this.domNode = e, this.menuitems = [], this.popups = [], this.menuitemGroups = {}, this.menuOrientation = {}, this.isPopup = {}, this.isPopout = {}, this.openPopups = !1, this.firstChars = {}, this.firstMenuitem = {}, this.lastMenuitem = {}, this.initMenu(e, 0), 
        e.addEventListener("focusin", this.onMenubarFocusin.bind(this)), 
        e.addEventListener("focusout", this.onMenubarFocusout.bind(this)), 
        window.addEventListener("pointerdown", this.onBackgroundPointerdown.bind(this), !0), 
        e.querySelector("[role=menuitem]").tabIndex = 0, 
        // APARTIR DE ACA SE HACE ALGO QUE TIENE QUE VER CON LA URL DONDE ESTA PARADO
        location.href.split("#").length > 1 ? 
        (t = location.href, i = function (e) {
                                                var t = e.split("#")[1];
                                                t = "string" == typeof t ? t.split("-").map(function (e) {
                                                    return e.charAt(0).toUpperCase() + e.slice(1)
                                                }).join(" ") : "Home";
                                                return t
                                            }(location.href)) : 
        (t = location.href + "/", i = "index") 
    }
    getParentMenuitem(e) {
        var t = e.parentNode;
        return !!(t && (t = t.parentNode) && (t = t.previousElementSibling) && "menuitem" === t.getAttribute("role")) && t
    }

    getMenuitems(e, t) {
        var i = [],
            s = this.initMenu.bind(this),
            n = this.popups;
        return function e(o) {
            for (var r, u; o;) {
                switch (u = !0, (r = o.getAttribute("role")) && (r = r.trim().toLowerCase()), r) {
                    case "menu":
                        o.tabIndex = -1, s(o, t + 1), u = !1;
                        break;
                    case "menuitem":
                        "true" === o.getAttribute("aria-haspopup") && n.push(o), i.push(o)
                }
                u && o.firstElementChild && "svg" !== o.firstElementChild.tagName && e(o.firstElementChild), o = o.nextElementSibling
            }
        }(e.firstElementChild), i
    }
    initMenu(e, t) {
        var i, s, n = this.getMenuId(e);
        i = this.getMenuitems(e, t), 
        this.menuOrientation[n] = this.getMenuOrientation(e), 
        this.isPopup[n] = "menu" === e.getAttribute("role") && 1 === t, 
        this.isPopout[n] = "menu" === e.getAttribute("role") && t > 1, 
        this.menuitemGroups[n] = [], this.firstChars[n] = [], 
        this.firstMenuitem[n] = null, this.lastMenuitem[n] = null;
        
        for (var o = 0; o < i.length; o++)(s = i[o]).getAttribute("role").indexOf("menuitem") < 0 || 
        (
            s.tabIndex = -1, 
            this.menuitems.push(s), 
            this.menuitemGroups[n].push(s), 
            this.firstChars[n].push(s.textContent.trim().toLowerCase()[0]), 
            s.addEventListener("keydown", this.onKeydown.bind(this)), 
            // Se cambió el click por el tab para que mencione que esta desplegable 
            // s.addEventListener("Click", this.onMenuitemClick.bind(this), { capture: !0 }),
            s.addEventListener("click", this.onMenuitemClick.bind(this), { capture: !0 }),         
            s.addEventListener("pointerover", this.onMenuitemPointerover.bind(this)), this.firstMenuitem[n] || (this.hasPopup(s) && (s.tabIndex = 0), this.firstMenuitem[n] = s), this.lastMenuitem[n] = s
        )
    }

    setFocusToMenuitem(e, t) {
        this.closePopupAll(t), this.menuitemGroups[e] && this.menuitemGroups[e].forEach(function (e) {
            e === t ? (e.tabIndex = 0, t.focus()) : e.tabIndex = -1
        })
    }
    setFocusToFirstMenuitem(e) {
        this.setFocusToMenuitem(e, this.firstMenuitem[e])
    }
    setFocusToLastMenuitem(e) {
        this.setFocusToMenuitem(e, this.lastMenuitem[e])
    }
    setFocusToPreviousMenuitem(e, t) {
        var i, s;
        return t === this.firstMenuitem[e] ? i = this.lastMenuitem[e] : (s = this.menuitemGroups[e].indexOf(t), i = this.menuitemGroups[e][s - 1]), this.setFocusToMenuitem(e, i), i
    }
    setFocusToNextMenuitem(e, t) {
        var i, s;
        return t === this.lastMenuitem[e] ? i = this.firstMenuitem[e] : (s = this.menuitemGroups[e].indexOf(t), i = this.menuitemGroups[e][s + 1]), this.setFocusToMenuitem(e, i), i
    }
    setFocusToNextMenuitemTab(e, t) {
        var i, s;
        return t === this.lastMenuitem[e] ? (this.openPopups = !1, this.setMenubarDataExpanded("false"),  i = this.firstMenuitem[e], this.setFocusToMenuitem(e, i), i, this.closePopup(n)) : (s = this.menuitemGroups[e].indexOf(t), i = this.menuitemGroups[e][s + 1]), this.setFocusToMenuitem(e, i), i
    }
    setFocusByFirstCharacter(e, t, i) {
        var s, n;
        i = i.toLowerCase(), (s = this.menuitemGroups[e].indexOf(t) + 1) >= this.menuitemGroups[e].length && (s = 0), -1 === (n = this.getIndexFirstChars(e, s, i)) && (n = this.getIndexFirstChars(e, 0, i)), n > -1 && this.setFocusToMenuitem(e, this.menuitemGroups[e][n])
    }
    
    getIndexFirstChars(e, t, i) {
        for (var s = t; s < this.firstChars[e].length; s++)
            if (i === this.firstChars[e][s]) return s;
        return -1
    }

    isPrintableCharacter(e) {
        return 1 === e.length && e.match(/\S/)
    }

    getIdFromAriaLabel(e) {
        var t = e.getAttribute("aria-label");
        return t && (t = t.trim().toLowerCase().replace(" ", "-").replace("/", "-")), t
    }
    getMenuOrientation(e) {
        var t = e.getAttribute("aria-orientation");
        if (!t) switch (e.getAttribute("role")) {
            case "menubar":
                t = "horizontal";
                break;
            case "menu":
                t = "vertical"
        }
        return t
    }
    getMenuId(e) {
        for (var t = !1, i = e.getAttribute("role"); e && "menu" !== i && "menubar" !== i;)(e = e.parentNode) && (i = e.getAttribute("role"));
        return e && (t = i + "-" + this.getIdFromAriaLabel(e)), t
    }
    getMenu(e) {
        for (var t = e, i = e.getAttribute("role"); t && "menu" !== i && "menubar" !== i;)(t = t.parentNode) && (i = t.getAttribute("role"));
        return t
    }
    isAnyPopupOpen() {
        for (var e = 0; e < this.popups.length; e++)
            if ("true" === this.popups[e].getAttribute("aria-expanded")) return !0;
        return !1
    }
    setMenubarDataExpanded(e) {
        this.domNode.setAttribute("data-menubar-item-expanded", e)
    }
    isMenubarDataExpandedTrue() {
        return "true" === this.domNode.getAttribute("data-menubar-item-expanded")
    }
    openPopup(e, t) {
        var i = t.nextElementSibling;
        if (i) {
            var s = t.getBoundingClientRect();
            return this.isPopup[e] ? (i.parentNode.style.position = "relative", i.style.display = "block", i.style.position = "absolute", i.style.left = s.width + 10 + "px", i.style.top = "0px", i.style.zIndex = 100) : (i.style.display = "block", i.style.position = "absolute", i.style.left = "0px", i.style.top = s.height + 8 + "px", i.style.zIndex = 100), t.setAttribute("aria-expanded", "true"), this.setMenubarDataExpanded("true"), this.getMenuId(i)
        }
        return !1
    }
    closePopout(e) {
        for (var t, i = this.getMenuId(e), s = e; this.isPopup[i] || this.isPopout[i];) s = (t = this.getMenu(s)).previousElementSibling, i = this.getMenuId(s), t.style.display = "none";
        return s.focus(), s
    }
    closePopup(e) {
        var t, i = this.getMenuId(e),
            s = e;
        return this.isMenubar(i) ? this.isOpen(e) && (e.setAttribute("aria-expanded", "false"), e.nextElementSibling.style.display = "none") : ((s = (t = this.getMenu(e)).previousElementSibling).setAttribute("aria-expanded", "false"), s.focus(), t.style.display = "none"), s
    }
    doesNotContain(e, t) {
        return !t || !e.nextElementSibling.contains(t)
    }
    closePopupAll(e) {
        "object" != typeof e && (e = !1);
        for (var t = 0; t < this.popups.length; t++) {
            var i = this.popups[t];     
            if (this.doesNotContain(i, e) && this.isOpen(i)) {
                var s = i.nextElementSibling;
                s && (i.setAttribute("aria-expanded", "false"), s.style.display = "none")
            }
        }
    }
    hasPopup(e) {
        return "true" === e.getAttribute("aria-haspopup")
    }
    isOpen(e) {
        return "true" === e.getAttribute("aria-expanded")
    }
    isMenubar(e) {
        return !this.isPopup[e] && !this.isPopout[e]
    }
    isMenuHorizontal(e) {
        return "horizontal" === this.menuOrientation[e]
    }
    hasFocus() {
        return this.domNode.classList.contains("focus")
    }
    onMenubarFocusin() {
        this.domNode.classList.add("focus")
    }
    onMenubarFocusout() {
        this.domNode.classList.remove("focus")
    }
    onKeydown(e) {
        var t, i, s, n = e.currentTarget,
            o = e.key,
            r = !1,
            u = this.getMenuId(n);
        switch (o) {
            case " ":
            case "Enter":
                this.hasPopup(n) ? (this.openPopups = !0, i = this.openPopup(u, n), this.setFocusToFirstMenuitem(i)) : "#" !== n.href && (this.closePopupAll(), this.updateContent(n.href, n.textContent.trim()), this.setMenubarDataExpanded("false")), r = !0;
                break;
            case "Esc":
            case "Escape":
                this.openPopups = !1, s = this.closePopup(n), t = this.getMenuId(s), this.setMenubarDataExpanded("false"), r = !0;
                break;
            case "Up":
            case "ArrowUp":
                this.isMenuHorizontal(u) ? this.hasPopup(n) && (this.openPopups = !0, i = this.openPopup(u, n), this.setFocusToLastMenuitem(i)) : this.setFocusToPreviousMenuitem(u, n), r = !0;
                break;
            case "ArrowDown":
    
            case "Down":
                this.isMenuHorizontal(u) ? this.hasPopup(n) && (this.openPopups = !0, i = this.openPopup(u, n), this.setFocusToFirstMenuitem(i)) : this.setFocusToNextMenuitem(u, n), r = !0;
                break;
            case "Left":
            case "ArrowLeft":
                this.isMenuHorizontal(u) ? (s = this.setFocusToPreviousMenuitem(u, n), (this.isAnyPopupOpen() || this.isMenubarDataExpandedTrue()) && this.openPopup(u, s)) : this.isPopout[u] ? (s = this.closePopup(n), t = this.getMenuId(s), s = this.setFocusToMenuitem(t, s)) : (s = this.closePopup(n), t = this.getMenuId(s), s = this.setFocusToPreviousMenuitem(t, s), this.openPopup(t, s)), r = !0;
                break;
            case "Right":
            case "ArrowRight":
                this.isMenuHorizontal(u) ? (s = this.setFocusToNextMenuitem(u, n), (this.isAnyPopupOpen() || this.isMenubarDataExpandedTrue()) && this.openPopup(u, s)) : this.hasPopup(n) ? (i = this.openPopup(u, n), this.setFocusToFirstMenuitem(i)) : (s = this.closePopout(n), t = this.getMenuId(s), s = this.setFocusToNextMenuitem(t, s), this.openPopup(t, s)), r = !0;
                break;
            case "Home":
            case "PageUp":
                this.setFocusToFirstMenuitem(u, n), r = !0;
                break;
            case "End":
            case "PageDown":
                this.setFocusToLastMenuitem(u, n), r = !0;
                break;
            case "Tab":
                // this.openPopups = !1, this.setMenubarDataExpanded("false"), this.closePopup(n);
                // break;
                this.isMenuHorizontal(u) ? (s = this.setFocusToNextMenuitemTab(u, n), (this.isAnyPopupOpen() || this.isMenubarDataExpandedTrue()) && this.openPopup(u, s)) : this.hasPopup(n) ? (i = this.openPopup(u, n), this.setFocusToFirstMenuitem(i)) : (s = this.closePopout(n), t = this.getMenuId(s), s = this.setFocusToNextMenuitemTab(t, s), this.openPopup(t, s)), r = !0;
                
                    
            

                break;
            default:
                this.isPrintableCharacter(o) && (this.setFocusByFirstCharacter(u, n, o), r = !0)
        }
        r && (e.stopPropagation(), e.preventDefault())
    }
    onMenuitemClick(e) {
        var t = e.currentTarget,
            i = this.getMenuId(t);
        this.hasPopup(t) ? this.isOpen(t) ? this.closePopup(t) : (this.closePopupAll(t), this.openPopup(i, t)) : this.closePopupAll();
    }
    onMenuitemPointerover(e) {
        var t = e.currentTarget,
            i = this.getMenuId(t);
        this.hasFocus() && this.setFocusToMenuitem(i, t), (this.isAnyPopupOpen() || this.hasFocus()) && (this.closePopupAll(t), this.hasPopup(t) && this.openPopup(i, t))
    }
    onBackgroundPointerdown(e) {
        this.domNode.contains(e.target) || this.closePopupAll()
    }
}
window.addEventListener("load", function () {
    for (var e = document.querySelectorAll(".menubar-navigation"), t = 0; t < e.length; t++){ 
        new MenubarNavigation(e[t])
    }
});