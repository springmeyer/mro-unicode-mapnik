import mapnik

m = mapnik.Map(256,256)
mapnik.load_map(m,'map.xml')
m.zoom_all()
im = mapnik.Image(m.width,m.height)
mapnik.render(m,im)
im.save('image.png')
print('check out image.png!')