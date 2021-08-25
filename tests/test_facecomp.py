import src.cw_nnrec.facecomp as facecomp


class TestFacecomp():
    def test_compare_equal(self):
        face1 = "tests/images/dicaprio1.jpg"
        face2 = "tests/images/dicaprio2.jpg"

        fc = facecomp.Facecomp()

        assert fc.add_faces(face1, face2) == True
        assert fc.compare() == True

    def test_compare_not_equal(self):
        face1 = "tests/images/dicaprio1.jpg"
        face2 = "tests/images/depp.jpg"

        fc = facecomp.Facecomp()

        assert fc.add_faces(face1, face2) == True
        assert fc.compare() == False
