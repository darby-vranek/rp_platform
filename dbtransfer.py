import psycopg2 as p
from apps.threads.models import Thread, Reply
from apps.characters.models import Character
from apps.verses.models import Verse
from apps.posts.models import Post
from apps.senpals.models import User

iris = User.objects.get(username='iris')


# transfer characters
conn = p.connect("dbname=rpbackup user=lyra")
c = conn.cursor()

c.execute("SELECT * FROM rp_character JOIN rp_profile ON rp_character.profile_ptr_id=rp_profile.id;")


for record in c:
	char = Character(
			user=iris,
			name=record[8],
			page_name=record[0],
			tagline=record[9],
			description=record[10],
			icon=record[1],
			header_image=record[2],
			created=record[6],
			updated=record[7]
		)
	char.save()

c.close()
conn.close()


# transfer verses


conn = p.connect("dbname=dcsqt67kp4mj5c user=lyra")
c = conn.cursor()

c.execute("SELECT * FROM rp_verse JOIN rp_profile ON rp_verse.profile_ptr_id=rp_profile.id;")


for record in c:
	v = Verse(
		admin=iris,
		name=record[5],
		franchise=record[0],
		description=record[6],
		created=record[3],
		updated=record[4]
	)
	v.save()


c.close()
conn.close()


# transfer posts
conn = p.connect("dbname=dcsqt67kp4mj5c user=lyra")
c = conn.cursor()

c.execute("SELECT * FROM rp_post JOIN rp_character ON rp_post.character_id=rp_character.profile_ptr_id JOIN rp_verse on rp_post.verse_id=rp_verse.profile_ptr_id;")

for record in c:
	if record[6]:
		char = Character.objects.get(page_name=record[7])
	else:
		char=None
	if record[11]:
		v = Verse.objects.filter(franchise=record[12]).first()
	else:
		v = None
	p = Post(
		user=iris,
		title=record[3],
		text=record[4],
		character=char,
		verse=v,
		created=record[1],
		updated=record[2]
	)
	p.save()

c.close()
conn.close()



# transfer threads
conn = p.connect("dbname=dcsqt67kp4mj5c user=lyra")
c = conn.cursor()

c.execute("SELECT * FROM rp_thread JOIN rp_verse ON rp_thread.verse_id=rp_verse.profile_ptr_id JOIN rp_profile ON rp_verse.profile_ptr_id=rp_profile.id;")

for record in c:
	if record[11]:
		v = Verse.objects.get(name=record[11])
	else:
		v = None
	t = Thread.objects.create(
		user=iris,
		title=record[3],
		verse=v,
		caption=record[4],
		created=record[1],
		updated=record[1]
	)



c.close()
conn.close()


# transfer replies
from apps.threads.models import Reply


conn = p.connect("dbname=dcsqt67kp4mj5c user=lyra")
c = conn.cursor()
c.execute("SELECT * FROM rp_reply JOIN rp_thread ON rp_reply.parent_id=rp_thread.id JOIN rp_character ON rp_reply.character_id=rp_character.profile_ptr_id;")

for record in c:
	char = Character.objects.get(page_name=record[12])
	thread = Thread.objects.get(title=record[9])
	r = Reply(
		character=char,
		thread=thread,
		text=record[3],
		created=record[1],
		updated=record[1]
	)
	r.save()




c.close()
conn.close()














