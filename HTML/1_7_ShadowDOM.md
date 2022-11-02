# Shadow Dom

**Shadow Dom 만드는 법**



```
<body>
    <div id="mordor"></div>
</body>
    <script>
        document.querySelector('#mordor').attachShadow({mode : 'open'})
        document.querySelector('#mordor').shadowRoot.innerHTML =
        '<p>안녕?</p>'
    </script>
```


<참고 자료>

[1](https://www.youtube.com/watch?v=o0spBNs0zRk)
