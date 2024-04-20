#+title: Troubleshooting

https://superuser.com/questions/1009571/how-to-prevent-url-redirects-in-chrome

```js
window.onbeforeunload = function(){ return 'Leave page?'; };
```

```js
window.addEventListener('beforeunload', (event) => {
  event.returnValue = `Are you sure you want to leave?`;
});
```
