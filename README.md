# download-gifyyy

Those Gifyyy URLs are pretty obvious. `/img123` can only suggest that there's an `/img122` and an `/img/124`, right? Well, who needs security by obscurity?  It's not clear whether all GIFs or just those that are sent are included.

Since Gifyyy uses MeteorJS to fetch image URLs, we use PhantomJS to render the page and scoop the URL.

Fortunately, this is easily parallelizable!

Assuming [GNU Parallel](http://www.gnu.org/software/parallel/)
`seq 1 1000 | parallel -j8 python --dest gifs/ --index {} <YourGalleryName>`
