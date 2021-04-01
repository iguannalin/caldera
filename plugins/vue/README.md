This project is an example of a plugin built with Vue, Tailwind, and Python/aiohttp that can be pulled into the CALDERA
core project. To recreate this plugin:

1. Edit/Create a vue.config.js in root/, with these settings:
```js
module.exports = {
    outputDir: 'templates',
    assetsDir: 'vue',
    indexPath: 'vue.html'
}
```
When you run the ```npm run build``` command, this will tell it to generate the static files into the templates/ directory.
The assetsDir should correlate to what you put into the hook.py file, so that the html file generated will know where to look for the assets.
For example, if your hook.py has this:
```python
app.router.add_static('/vue', 'plugins/vue/templates/vue', append_version=True)
```
Then your assetsDir should be:
```js
assetsDir: 'vue'
```
So now the hook will look inside templates/vue for your static assets, and npm run build will generate the static assets into templates/vue.
This is also important, so the generated index.html file will have the correct absolute paths to the static assets as well. 

The indexPath by default will be index.html, but can be changed if you wish the template to be named differently.
2. Modify the hook.py file, to include both the route to the static assets and a route that the core app should ping to reach the gui:
```python
app.router.add_static('/vue', 'plugins/vue/templates/vue', append_version=True)
app.router.add_route('GET', '/plugin/vue/gui', vue_gui.splash)
```
3. Make sure you have the files {{plugin_name}}_gui.py (which should call your template), {{plugin_name}}_api.py, and {{plugin_name}}_svc.py. 
