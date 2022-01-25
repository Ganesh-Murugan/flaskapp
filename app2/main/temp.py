import sqlite3
conn = sqlite3.connect('app2\main\Shop.db', check_same_thread=False)
cursor=conn.cursor()
r = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print(r)
<!-- <form method="post" class="topnav" action="{{url_for('index')}}">
        <select name="cat">
          <option value="" selected disabled hidden>Choose category</option>
          {% for o in x %}
              <option value="{{ o.id }}">{{ o.category_name }}</option>
              {% endfor %}
        </select>
        
        <input type="submit">
    </form> -->