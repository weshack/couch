// Generated by CoffeeScript 1.3.3
var autocomplete, courseTemplate, updateCourseResults;

courseTemplate = function(_arg) {
  var code, name, professor;
  code = _arg.code, name = _arg.name, professor = _arg.professor;
  return "<div class='course-result'>\n  <p class='course-result-code'>" + code + "</p\n  <p class='course-result-name'>" + name + "</p>\n  <p class='course-result-professor'>" + professor + "</p>\n</div>";
};

updateCourseResults = function(results) {
  var result, _i, _len, _results;
  $("#course-results").html('');
  _results = [];
  for (_i = 0, _len = results.length; _i < _len; _i++) {
    result = results[_i];
    _results.push($("#course-results").append(courseTemplate(result)));
  }
  return _results;
};

autocomplete = function(term) {
  return [
    {
      code: "ARHA385",
      name: "European Architecture to 1750",
      professor: "Siry,Joseph M."
    }, {
      code: "ARHA385",
      name: "European Architecture to 1750",
      professor: "Siry,Joseph M."
    }, {
      code: "ARHA385",
      name: "European Architecture to 1750",
      professor: "Siry,Joseph M."
    }, {
      code: "ARHA385",
      name: "European Architecture to 1750",
      professor: "Siry,Joseph M."
    }
  ];
};

$(function() {
  return $("#course-search").on('input', function() {
    var courseResults;
    courseResults = autocomplete(this.value);
    return updateCourseResults(courseResults);
  });
});
