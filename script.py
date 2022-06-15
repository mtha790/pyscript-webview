try:
    from pyscript import *
    raise Exception
except Exception:
    pass
            
some_html = f"""
<div>
    <p>Once upon a time ...</p>
</div>
"""

root = Element("root")
root.write(some_html)