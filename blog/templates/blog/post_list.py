<html>
<head>
<title>Django Girls blog</title>
</head>
<body>
<div>
<h1><a href="/">Django Girls Blog</a></h1>
</div>
<div>
<h1><a href="/">Django Girls Blog</a></h1>
</div>
{% for post in posts %}
<div>
<p>published: {{ post.published_date }}</p>
<h2><a href="">{{ post.title }}</a></h2>
<p>{{ post.text|linebreaksbr }}</p>
</div>
{% endfor %}
</body>
</html>