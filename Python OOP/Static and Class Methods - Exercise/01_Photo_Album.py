import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        for page in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(math.ceil(photos_count/4))

    def add_photo(self, label):
        is_added = False
        for idx, page in enumerate(self.photos):
            if len(self.photos[idx]) < 4:
                self.photos[idx].append(label)
                is_added = True
                return f"{label} photo added successfully on page {idx+1} slot {len(self.photos[idx])}"
        if not is_added:
            return "No more free slots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            result += f"{'[] '*len(page)}".rstrip()
            result += "\n"
            result += "-----------\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
