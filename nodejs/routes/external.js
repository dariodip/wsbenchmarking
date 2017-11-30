const express = require('express');
const router = express.Router();
const request = require('request');

const externalResourceURL = "https://jsonplaceholder.typicode.com";


router.get('/posts', function(req, res, next) {
    res.setHeader('Content-Type', 'application/json');
    let url = externalResourceURL + '/posts';
    request(url, function(error, response, body) {
        if (error || !response) {
            console.error(error);
            next(error);
            return;
        }
        if (response.statusCode === 200) {
            res.send(JSON.parse(body));
            return;
        }
        res.send({"error" : "Status code was " + response.statusCode});
    });
});

router.get('/albums', function(req, res, next) {
    res.setHeader('Content-Type', 'application/json');
    let url = externalResourceURL + "/albums";
    request(url, function(error, response, body) {
        if (error || !response) {
            console.error(error);
            next(error);
            return;
        }
        if (response.statusCode === 200) {
            res.send(JSON.parse(body));
            return;
        }
        res.send({"error" : "Status code was " + response.statusCode});
    });
});

router.get('/photos', function(req, res, next) {
    res.setHeader('Content-Type', 'application/json');
    let url = externalResourceURL + "/photos";
    request(url, function(error, response, body) {
        if (error || !response) {
            console.error(error);
            next(error);
            return;
        }
        if (response.statusCode === 200) {
            res.send(JSON.parse(body));
            return;
        }
        res.send({"error" : "Status code was " + response.statusCode});
    });
});

router.get('/albums_w_photos', function(req, res, next) {
    res.setHeader('Content-Type', 'application/json');
    let urlPhoto = externalResourceURL + "/photos";
    let urlAlbum = externalResourceURL + "/albums";
    request(urlAlbum, function(error, response, body){
        if (error || !response) {
            console.error(error);
            next(error);
            return;
        }
        if (response.statusCode === 200) {
            let albumList = getAlbumList(response.body);
            request(urlPhoto, function(photoError, photoResponse, photoBody) {
                if (photoError || !photoResponse) {
                    console.error(photoError);
                    next(photoError);
                    return;
                }
                if (photoResponse.statusCode !== 200) {
                    res.send({"error": "Error while trying to retrieve photos. Status code: " + response.statusCode});
                    return;
                }
                let photoList = getPhotoList(photoBody);
                let albumsWithPhotos = mergeAlbumsAndPhotos(albumList, photoList);
                res.send(albumsWithPhotos.slice(1));
            });
            return;
        }
        res.send({"error": "Error while trying to retrieve albums. Stauts code: " + response.statusCode});
    });
});

function getAlbumList(albumString) {
    let albs = JSON.parse(albumString);
    let albumArray = [];
    if (typeof albs === typeof [] && albs.length > 0) {
        for (let i in albs) {
            albumArray[albs[i].id] = albs[i];
        }
    } else {
        return [];
    }
    return albumArray;
}

function getPhotoList(photoString) {
    let phs = JSON.parse(photoString);
    let photoArray = [];
    if (typeof phs === typeof [] && phs.length > 0) {
        for (let i in phs) {
            photoArray[phs[i].id] = phs[i];
        }
    } else {
        return [];
    }
    return photoArray;
}

function mergeAlbumsAndPhotos(albumList, photoList) {
    for (let pId in photoList) {
        let photo = photoList[pId];
        let albumId = photo['albumId'];
        let album = albumList[albumId];
        if ('photos' in album) {
            album['photos'].push(photo);
        } else {
            album['photos'] = [photo];
        }
    }
    return albumList;
}

module.exports = router;