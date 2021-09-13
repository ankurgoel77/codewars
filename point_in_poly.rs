// https://www.codewars.com/kata/530265044b7e23379d00076a/train/rust

type Point = (f32, f32);

fn point_in_poly(poly: &[Point], point: Point) -> bool {
    // use ray hit casting method : https://en.wikipedia.org/wiki/Point_in_polygon
    let mut num_hits:i32 = 0;

    let (pt_x, pt_y) = point;

    // cast a ray in the positive y direction from our point. We do that by solving for the line equation for each edge, and then checking if y value 
    // of the line is larger than the y value of the point. We also need to check if the x values of the edge points straddle the x value of our test point
    
    for i in 0..poly.len() {
        let mut j = i+1;
        if i == poly.len()-1 {
            j = 0;
        }
        let m = (poly[j].1 - poly[i].1) / (poly[j].0 - poly[i].0);
        let b = poly[i].1 - m*poly[i].0;
        let y = m*pt_x + b;
        if y > pt_y && ( (poly[i].0 < pt_x  && poly[j].0 > pt_x) || (poly[i].0 > pt_x && poly[j].0 < pt_x) ) {
            num_hits += 1;
        }
    }
    
    // if num_hits is even, point is outside poly, else it's inside poly
    match num_hits % 2 {
        0 => false,
        _ => true,
    }
}