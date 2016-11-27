function update_scraper_summary(){

    $.getJSON("/scraper_summary", function(data){
//        console.log(data);
    });
};

couchbase = function update_couchbase_summary(){i

    $.getJSON("/couchbase_summary", function(data){
//        console.log(data);
    });

};
