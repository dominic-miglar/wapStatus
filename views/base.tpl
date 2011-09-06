<!DOCTYPE html>

<html>
    <head>
        {% block head %}
        <link rel="stylesheet" type="text/css" href="styles/main.css" />
        <title>{% block title %}no title{% endblock title %}</title>
        {% endblock head %}
    </head>

    <body>
        <div id="container">
            {% block content %}
                <p>no content</p>
            {% endblock content %}
        </div>
    </body>
</html>
