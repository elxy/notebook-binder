# cp this file to ~/.ipython/profile_default/
c = get_config()
c.InlineBackend.figure_formats = ['svg']
c.IPKernelApp.matplotlib = 'inline'
c.InlineBackend.rc = {
    'figure.dpi': 96,
    'svg.hashsalt': 'python-audio',
}
