import argparse

import cw_nnrec.facecomp as facecomp


def main():
    parser = argparse.ArgumentParser(
        description="course work with neural networking")
    parser.add_argument(
        '-f', '--faces', help='compare two photo with faces', nargs='+')
    parser.add_argument(
        '-t', '--threshold', help='set threshold value for comparison (0..1)',
        nargs='?', type=float, const=0.6)

    args = parser.parse_args()

    if args.faces:
        face1 = args.faces[0]
        face2 = args.faces[1]

        fc = facecomp.Facecomp(args.threshold)

        if fc.add_faces(face1, face2):
            print(f"{fc.compare()}")
        else:
            print("Wrong path(s)!")


if __name__ == "__main__":
    main()
