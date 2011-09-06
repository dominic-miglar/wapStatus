{% extends "base.tpl" %}

{% block title %}
    wapstatus 0.1
{% endblock title %}

{% block content %}
    <h2>WAP Status Page</h2>
    <table>
        <tr>
            <th>Service</th>
            <th>Status</th>
        </tr>
        {% for service, status in statuses %}
            <tr>
                <td>{{ service }}</td>
                {% if status is sameas 'Offline' %}
                    <td class="offline">{{ status }}</td>
                {% else %} 
                    <td class="online">{{ status }}</td>
                {% endif %}
            </tr>
        {% endfor %}   
    </table>
    <p>Copyright 2011 by war10ck@serverkiller.net</p>
{% endblock content %}
