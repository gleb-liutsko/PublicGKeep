from . import app
from . import config
from . import function
from flask import render_template
import json
import gkeepapi
import os

@app.route('/')
def index():
	keep = function.get_gkeep()

	notes = []
	for i in keep.find(labels=[keep.findLabel(config.TAG_PUBLIC)], archived=False):
		notes.append({
			'title': i.title,
			'id': i.id
		})

	return render_template(
		'index.html',
		name_site=config.NAME_SITE,
		copyright_text=config.COPYRIGHT_TEXT,
		copyright_url=config.COPYRIGHT_URL,
		notes=notes
	)

@app.route('/note/<string:id_note>/')
def note(id_note):
	keep = function.get_gkeep()

	note = keep.get(id_note)
	img_links = []
	if len(note.blobs) > 0:
		for i in note.blobs:
			if str(note.blobs[0].blob.type) == 'BlobType.Image':
				img_links.append(keep.getMediaLink(i))
	print(type(img_links))
	return render_template(
		'note.html',
		name_site=config.NAME_SITE,
		copyright_text=config.COPYRIGHT_TEXT,
		copyright_url=config.COPYRIGHT_URL,
		note_title=note.title,
		note_text=note.text.replace('\n', '<br>'),
		img_links=img_links
	)
