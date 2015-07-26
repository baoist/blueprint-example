from flask import Blueprint, render_template, request

index = Blueprint('index', __name__,
                  template_folder="index",
                  static_folder="static")

@index.route('/foo')
def foo():
    foo = "bar"
    return render_template('index/foo.html', foo=foo)

@index.route('/bar', methods=["POST"])
def bar():
    params = request.form
    return render_template('index/foo.html', foo=params['random_input_name'])
